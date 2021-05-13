import sys
#input = sys.stdin.buffer.readline
from collections import Counter

def main():
    N,P = map(int,input().split())
    S = input()
    
    if 10%P == 0:
        ans = 0
        for i,st in enumerate(S[::-1]):
            num = int(st)
            if num % P == 0:
                ans += N-i
    else:
        ans,base = 0,1
        MOD_list = [0]
        for st in S[::-1]:
            num = int(st)
            MOD = (MOD_list[-1]+num*base)%P
            MOD_list.append(MOD)
            base *= 10
            base %= P
        c = Counter(MOD_list)
        for v in c.values():
            ans += (v*(v-1))//2
        
    print(ans)

if __name__ == "__main__":
    main()
