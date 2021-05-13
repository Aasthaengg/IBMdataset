S = input()

print(["YES", "NO"][not(8 <= ((15 - len(S)) + S.count("o")))])
