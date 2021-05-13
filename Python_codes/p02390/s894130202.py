S = int(input())
h = S // 3600   #切り捨て除算⇒//
m = (S - h * 3600) // 60
s = S - (h * 3600 + m * 60)
print(h, ":", m, ":", s, sep = "")
