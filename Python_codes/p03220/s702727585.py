N = int(input())
T, A = map(int, input().split())
lis = list(map(int, input().split()))

def calc_tem(H):
    return abs(A - ((T*1000) - (H*6)) / 1000)

new_lis = list(map(calc_tem, lis))
ans = new_lis.index(min(new_lis)) + 1

print(ans)