#入力処理
A, B, M = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
kingaku=[]
for i in range(M):
    x_input, y_input, c_input = map(int, input().split())
    kingaku.append(a[x_input-1]+b[y_input-1]-c_input)
kingaku.append(min(a)+min(b))

print(min(kingaku))