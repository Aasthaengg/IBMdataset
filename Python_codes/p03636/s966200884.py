list_S = input()
num = len(list_S)-2
num = str(num)
f = list_S[0]
l = list_S[-1]
ans = [f, num, l]
print("".join(ans))