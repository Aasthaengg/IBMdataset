# coding:utf-8
# 演算を辞書に押し込む
ops = {	"+": lambda a, b: b + a,
		"-": lambda a, b: b - a,
		"*": lambda a, b: b * a,
		"/": lambda a, b: b / a}

stack = []

for s in raw_input().split():
	if s in ops:
		stack.append(ops[s](stack.pop(), stack.pop()))
	else:
		stack.append(int(s))
print stack[-1]		