def main():
    S = input()
    odd_list=['R', 'U', 'D']
    eve_list=['L', 'U', 'D']
    odd = S[0::2]
    eve = S[1::2]
    for i in odd:
        if i not in odd_list:
            print('No')
            return
    for i in eve:
        if i not in eve_list:
            print('No')
            return
    print('Yes')

main()
