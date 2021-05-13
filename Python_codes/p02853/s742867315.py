import heapq
from sys import stdin
input = stdin.readline

#入力
# s = list(input()[0:-1])
# n = int(input())
x = list(map(int, input().split()))
# a = list(map(int,input().split()))
# b = list(map(int,input().split()))
# w = [int(input()) for i in range(n)]

# ab=[]
# for i in range(N):
#     a,b = map(int, input().split())
#     ab.append((a,b))
 
def main():
    sal = {1:(3*10**5),2:2*(10**5),3:10**5}
    ans = 0
    for i in x:
        if i not in sal:
            continue
        ans+=sal[i]
    if x[0]==1 and x[1]==1:
        ans+=4*(10**5)
    print(ans)

if __name__ == '__main__':
    main()