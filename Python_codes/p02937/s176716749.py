import sys
#input = sys.stdin.buffer.readline
import bisect

def main():
    s = input()
    t = input()
    
    index = [[] for _ in range(26)]
    for x,st in enumerate(s):
        index[ord(st)-ord("a")].append(x)
    
    roop,now = 0,-1
    for st in t:
        num = ord(st)-ord("a")
        if index[num] == []:
            print(-1)
            exit()
        else:
            pos = bisect.bisect_right(index[num],now)
            if pos == len(index[num]):
                roop += 1
                now = index[num][0]
            else:
                now = index[num][pos]
                
    print(roop*len(s)+now+1)
    
if __name__ == "__main__":
    main()