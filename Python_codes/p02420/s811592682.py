def main():

    data = ()
    shuffles = ()
    
    while True:
        input_text = input()
        if input_text == '-': break
        data += (input_text,)
        shuffle_length = int(input())
        shuffles += (sum(int(input()) for i in range(shuffle_length)),)

    for text, shuffles in zip(data, shuffles):
        print(text[(shuffles % len(text)):] + text[:(shuffles % len(text))])
main()