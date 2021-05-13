n = int(input())
p = [int(input()) for _ in range(n)]
# N 個のうち最も定価が高い品物 1 個を定価の半額で買うことができる。
m = max(p)
print(sum(p)-m//2)
