S = input()
print("YES" if S.count("o") >= abs(len(S)-7) or len(S) < 8 else "NO")