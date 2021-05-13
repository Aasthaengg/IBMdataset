ST = [input(),input()]
ST = [int(i) for i in range(3) if ST[0][i] == ST[1][i]]
print(len(ST))