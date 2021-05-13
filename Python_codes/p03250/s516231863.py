def LI(): return list(map(int, input().split()))


A,B,C = LI()
max_value = max([A*10+B+C,A+B*10+C,A+B+C*10])

print(max_value)