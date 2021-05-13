O = input()
E = input()

ans = ''.join(''.join(s) for s in zip(O, E))
ans += O[-1] if len(O) - len(E) == 1 else ''
print(ans)