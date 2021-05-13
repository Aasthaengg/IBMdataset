C = input()
chars = "abcdefghijklmnopqrstuvwxyz"
ls = list(chars) + list(chars)
dic = {ls[i]:ls[i+1] for i in range(26)}
print(dic[C])