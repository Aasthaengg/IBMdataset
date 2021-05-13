a,b,t = map(int, input().split())
if a > t:
    print(0)
else:
    tempo = int((t + 0.5) / a)
    print(tempo * b)