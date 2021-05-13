from collections import deque
def main():
    n=int(input())
    d=sorted(map(int,input().split()))
    m=int(input())
    t=deque(sorted(map(int,input().split())))
    
    for i in d:
        if t[0] == i:
            t.popleft()
            if len(t) == 0:
                print("YES")
                break
        elif t[0] < i:
            print("NO")
            break
    else:
        print("NO")
        
if __name__ == "__main__":
    main()