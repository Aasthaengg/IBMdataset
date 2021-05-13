#他の方の解答を参考にさせていただきました。
dic = {}
n = int(input())
for i in range(n):
	s = input()
	if s[0] == 'i': dic[s[7:]] = "a"
	else: print("yes" if s[5:] in dic else "no")
