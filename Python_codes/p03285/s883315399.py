print("Yes" if [4*i+7*j for i in range(26) for j in range(16)].count(int(input()))  else "No")