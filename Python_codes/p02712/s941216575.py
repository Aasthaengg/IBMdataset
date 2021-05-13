def total_n(n):
    return (n * (n+1)) / 2

n = int(input())
ans = total_n(n) - total_n(n//3)*3 - total_n(n//5)*5 + total_n(n//15)*15
print(int(ans))