S=input()
T=input()
print("Yes" if S==T[:len(T)-1] and len(S)+1==len(T) else "No")