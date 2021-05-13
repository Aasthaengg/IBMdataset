n = int(input())
a_s = list(map(int, input().split(' ')))
b_s = list(map(int, input().split(' ')))
c_s = list(map(int, input().split(' ')))

sat = 0
for a_i in range(0, n):
    i = a_s[a_i] - 1
    b = b_s[i]
    sat += b
    if a_i < n-1 and a_s[a_i] +1 == a_s[a_i+1]:
        if i >= 0:
            sat += c_s[i]
print(sat)