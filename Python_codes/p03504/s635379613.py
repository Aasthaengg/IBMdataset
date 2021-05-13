from sys import stdin

def getval():
    n,c = map(int,stdin.readline().split())
    s = [list(map(int,stdin.readline().split())) for i in range(n)]
    return n,c,s

def main(n,c,s):
    arr = [[0 for i in range(c)] for i in range(10**5)]
    for i in s:
        ch = i[2]-1
        for j in range(i[0]-1,i[1]):
            arr[j][ch] = 1
    ans = 0
    for i in range(10**5):
        loc = arr[i]
        temp = 0
        for j in range(c):
            temp += loc[j]
        ans = max(temp,ans)
    print(ans)

if __name__=="__main__":
    n,c,s = getval()
    main(n,c,s)