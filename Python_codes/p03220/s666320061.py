n = int(input())
t, a = map(int, input().split())
h = list(map(int,input().split()))
temp = [0] * n
def func(x) :
    return abs(x-a)
for i in range(n) :
    temp[i] = t - h[i] * 0.006
diff = list(map(func, temp))
mn_index = diff.index(min(diff))
print(mn_index+1)
