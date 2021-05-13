s = input()
t = input()

s_char = [x for x in s]
t_char = [x for x in t]

s_char.sort()
t_char.sort(reverse=True)

new_s = ''
new_t = ''

for x in s_char:
    new_s += x

for x in t_char:
    new_t += x

print('Yes' if new_s < new_t else 'No')
