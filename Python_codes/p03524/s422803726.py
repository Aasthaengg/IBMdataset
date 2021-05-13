S=input()
li=[S.count("a"),S.count("b"),S.count("c")]
print("YES" if max(li)-min(li)<=1 else "NO")
