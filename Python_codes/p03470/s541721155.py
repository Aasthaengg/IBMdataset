N = int(input())
num = [0 for _ in range(110)]

for i in range(N):
    d = int(input())
    num[d] = 1 # 複数個あっても 1 にしておく
print(sum(num))