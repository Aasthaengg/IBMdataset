N = int(input())
moji = str(input())

print(("No","Yes")[moji[:int(N/2)] == moji[int(N/2):]])