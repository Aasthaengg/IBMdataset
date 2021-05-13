S, C = map(int, input().split())
print(min(S, C//2) if S*2 >= C else (S*2+C)//4)