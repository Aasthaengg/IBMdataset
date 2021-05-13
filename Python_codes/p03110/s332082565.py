N = int(input())
price = [list(input().split()) for _ in range(N)]
count = [int(i[0]) if i[1] == 'JPY' else float(i[0])*380000.0 for i in price]
print(sum(count))