n = int(input())
a = list(map(int, input().split()))
ans = 0
def division2(x) :
    cnt = 0
    while x%2 == 0 :
        x //= 2
        cnt += 1
    return cnt
def count2(list) :
    ans = 0
    for i in range(len(list)) :
        ans += division2(list[i])
    return ans

print(count2(a))
