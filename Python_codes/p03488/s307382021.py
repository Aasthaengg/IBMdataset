import sys
#input = sys.stdin.buffer.readline

def main():
    s = input().split("T")
    x,y = map(int,input().split())
    l = len(s)
    dx,dy = [len(s[0])],[0]
    nx,ny = [],[]
    for i in range(1,l):
        d = len(s[i])
        if i%2 == 0:
            nx = []
            for num in dx:
                nx.append(num+d)
                nx.append(num-d)
            dx = list(set(nx))
        else:
            ny = []
            for num in dy:
                ny.append(num+d)
                ny.append(num-d)
            dy = list(set(ny))

    if (x in dx and y in dy):
        print("Yes")
    else:
        print("No")
    
if __name__ == "__main__":
    main()
