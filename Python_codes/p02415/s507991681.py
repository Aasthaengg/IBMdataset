#coding:utf-8
#??????????????????????????§??§??????????°??????????????°????????????§???????????????????????????

text = list(raw_input())
for i in range(len(text)) :
	if ord(text[i])<=90 and ord(text[i])>=65:
		text[i] = chr(ord(text[i])+32)
	elif ord(text[i])<=122 and ord(text[i])>=97:
		text[i] = chr(ord(text[i])-32)
print(''.join(text))