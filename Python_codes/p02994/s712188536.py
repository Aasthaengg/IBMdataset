N,L = map(int, input().split())

apple = [L+i for i in range(N)]
min = 500
for k in range(len(apple)):
    if abs(apple[k])<abs(min):
        min = apple[k]

apple.remove(min)
print(sum(apple))