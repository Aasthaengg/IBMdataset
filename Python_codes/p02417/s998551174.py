import sys
import string

text = ""
for line in sys.stdin:
    text += line

character_count_map = {}

for c in text.lower():
    if c not in character_count_map:
        character_count_map[c] = 0
    character_count_map[c] += 1

for c in string.ascii_lowercase:
    if c in character_count_map:
        print(c, ":", character_count_map[c])
    else:
        print(c, ":", 0)