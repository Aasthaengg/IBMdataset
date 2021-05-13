n = input()

def main(num):
    for i in num:
        if i == '9':
            return 'Yes'
    else:
        return 'No'

print(main(n))