button=list(map(int,input().split()))
button.sort()
sco = 0
sco += button[1]
button[1] -= 1
button.sort()
sco += button[1]
print(sco)