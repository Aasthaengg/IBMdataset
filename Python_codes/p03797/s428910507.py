n, m = map(int, input().split())

if n == m/2:
    print(n)
elif n < m/2:  # cが余る（c4つでscc1つ）
    print(n + (m-2*n)//4)
elif n > m/2:  # cが足りない
    print(m//2)