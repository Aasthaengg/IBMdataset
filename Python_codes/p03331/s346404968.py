n=input()
ai=0
if int(n) % 10 != 0:
    for i in range(len(n)):
        ai += int(n[i])
else:
    ai = 10
print(ai)