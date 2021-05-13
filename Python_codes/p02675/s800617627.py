N = input()
h = list('24579')
p = list('0168')
if N[-1] in h:
    o = 'hon'
elif N[-1] in p:
    o = 'pon'
else:
    o = 'bon'
print(o)