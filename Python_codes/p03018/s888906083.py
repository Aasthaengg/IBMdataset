s = input()
pos = 0
str_len = len(s)
count = 0
seq_a = 0
seq_bc = 0

while pos < str_len:
    if s[pos] == "A":
        while pos < str_len and s[pos] == "A":
            seq_a += 1
            pos += 1
        if pos+1 < str_len and s[pos] == "B" and s[pos + 1] == "C":
            while pos < str_len and s[pos] == "B" and pos + 1 < str_len and s[pos + 1] == "C":
                seq_bc += 1
                pos += 2
            count += seq_a * seq_bc
            if pos < str_len and s[pos] != "A":
                seq_a = 0
            seq_bc = 0
        else:
            pos += 1
            seq_a = 0
    else:
        pos += 1
        seq_a = 0

print(count)
