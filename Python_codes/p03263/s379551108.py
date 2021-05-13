import math
def main():
    h,w = map(int,input().split())
    Map = []
    ans = []
    for i in range(h):
        tmp = [int(i) for i in input().split()]
        Map.append(tmp)
    for i in range(h-1):
        for j in range(w):
            if Map[i][j]%2==1:
                Map[i][j]-=1
                Map[i+1][j] += 1
                ans.append([i+1,j+1,i+2,j+1])
    for j in range(w-1):
        if Map[h-1][j]%2==1:
            Map[h-1][j] -= 1
            Map[h-1][j+1] += 1
            ans.append([h,j+1,h,j+2])
    ans_l = len(ans)
    print(ans_l)
    for i in range(ans_l):
        print(*ans[i])
main()
