alpha = 'abcdefghijklmnopqrstuvwxyz'
text = ''

while True:
    try:
        text += input().lower()
    except:
        break
        
for key in alpha:
        print('{} : {}'.format(key, text.count(key)))
