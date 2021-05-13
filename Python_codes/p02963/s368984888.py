S = int(input())

v = 10**9
a = (v-S%v)%v
b = (S+a)//v

print(0, 0, 10**9, 1, a, b)