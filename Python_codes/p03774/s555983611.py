import itertools,collections
def main():
    n,m=map(int, input().split())
    pos = []
    checkp = []
    for i in range(n):
        a,b=map(int, input().split())
        pos.append((a,b))
    for i in range(m):
        c,d = map(int, input().split())
        checkp.append((c,d))

    res = []
    for i in range(n):
        shortes = 10000000000
        index = 1000
        for j in range(m):
            if(shortes>abs(pos[i][0]-checkp[j][0]) + abs(pos[i][1]-checkp[j][1])):
                shortes=abs(pos[i][0]-checkp[j][0]) + abs(pos[i][1]-checkp[j][1])
                index = j

        res.append(index+1)
    for i in res:
        print(i)

if __name__ == '__main__':
    main()
