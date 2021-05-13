a,b = input().split()
dic = {"H":True,"D":False}
a = dic[a]
b = dic[b]
print("D" if a^b else "H")