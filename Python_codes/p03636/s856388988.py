letter = list(map(str, input()))
ans = letter[0] + str(len(letter)-2) + letter[-1]
print(ans)
