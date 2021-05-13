N = int(input())
Ai = list(map(int,input().split()))
Alice = 0
Bob = 0
Ai.append(0)

while Ai:
    Alice += max(Ai)
    Ai.remove(max(Ai))
    if not Ai:
        break
    Bob += max(Ai)
    Ai.remove(max(Ai))

print(Alice-Bob)