def text_print(text, a, b):
    print(text[a:b + 1])


def text_reverse(text, a, b):
    return text[:a] + text[a:b + 1][::-1] + text[b + 1:]


def text_replace(text, a, b, replaced_text):
    return text[:a] + replaced_text + text[b + 1:]


text = raw_input()
num = int(raw_input())

while 0 < num:
    raw = raw_input().split()
    if raw[0] == "replace":
        text = text_replace(text, int(raw[1]), int(raw[2]), raw[3])
    elif raw[0] == "reverse":
        text = text_reverse(text, int(raw[1]), int(raw[2]))
    elif raw[0] == "print":
        text_print(text, int(raw[1]), int(raw[2]))
    num -= 1