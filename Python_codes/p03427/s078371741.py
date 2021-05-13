n = list(map(int, input()))
l = [sum(n)]
for i in range(1, len(n)):
    n[-i] = 9
    n[-i-1] -= 1
    l.append(sum(n)) 
print(max(l))