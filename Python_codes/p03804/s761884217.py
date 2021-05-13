#k = int(input())
#s = input()
#a, b = map(int, input().split())
#s, t = map(str, input().split())
#l = list(map(int, input().split()))
#l = [list(map(int,input().split())) for i in range(n)]
#a = [list(input()) for _ in range(n)]

def equal(a, b, i,j,m):
    for k in range(m):
        for l in range(m):
            if a[i+k][j+l] != b[k][l]:
                return False
    return True


#n = ["abc","cde","xzy"]
#m = ["abc","cde","jzy"]
a = []
b = []
n,m = map(int, input().split())
a = [list(input()) for _ in range(n)]
b = [list(input()) for _ in range(m)]

temp = n - m + 1


for i in range(temp):
    for j in range(temp):
        #[i][j]を起点として比較
        for k in range(m):
            for l in range(m):
                if equal(a,b,i,j,m):
                    print("Yes")
                    exit()
print("No")



