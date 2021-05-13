W = input()
print("Yes" if all(W.count(w)%2==0 for w in W) else "No")